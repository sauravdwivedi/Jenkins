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
    sh "docker compose -f $DOCKER_COMPOSE_FILE up -d $serviceName"
}

def checkContainerLogs(serviceName) {
    sh(
        returnStdout: true, 
        returnStatus: true, 
        script: "echo $ASTERISKS-$serviceName-logs-$ASTERISKS"
    )
    serviceContainer = sh(
        script: "docker container ls | grep jenkins-$serviceName | awk '{print \$1}'", 
        returnStdout: true
    )
    if (serviceContainer != "") {
        sh "docker logs jenkins-$serviceName"
    } else {
        sh "echo No containers found"
    }
}

return this