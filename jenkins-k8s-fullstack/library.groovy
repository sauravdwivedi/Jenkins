def loginToDockerRegistry() {
    sh "docker login -u $REGISTRY_CREDENTIAL_USR -p $REGISTRY_CREDENTIAL_PSW"
}

def buildTagAndPushContainer(serviceName, imageName) { 
    loginToDockerRegistry()
    dockerImage = docker.build(
        "$REGISTRY/$imageName:$BUILD_NUMBER", 
        "$WORK_DIR/$serviceName"
    )
    dockerImage.push()
    dockerImage.push('latest')
}

def deployContainer(serviceName) {
    sh "kubectl create namespace $serviceName || true"
    sh "kubectl apply -f $WORK_DIR/k8s/$serviceName-deployment.yaml -n $serviceName"
}

def checkContainerLogs(serviceName) {
    sh(
        returnStdout: true, 
        returnStatus: true, 
        script: "echo $ASTERISKS-$serviceName-logs-$ASTERISKS"
    )
    servicePod = sh(
        script: "kubectl get pods -n $serviceName --no-headers -o custom-columns=:metadata.name | head -1", 
        returnStdout: true
    )
    if (servicePod != "") {
        sh "kubectl logs -n $serviceName $servicePod"
    } else {
        sh "echo No pods found in the namespace $serviceName"
    }
}

return this;