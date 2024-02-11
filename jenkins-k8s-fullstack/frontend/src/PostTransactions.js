import "./App.css";
import {useState} from "react";
import List from '@mui/material/List';
import ListItem from '@mui/material/ListItem';

function PostTransactions() {
  const [account_id, setAccountID] = useState("");
  const [amount, setAmount] = useState("");
  const [balance, setBalance] = useState("");
  const [history, setHistory] = useState("");
  const [message, setMessage] = useState("");
  const [summary, setSummary] = useState("");

  let handleSubmit = async (e) => {
    e.preventDefault();
    try {
      let res = await fetch("http://127.0.0.1:5000/api/v1/transactions", {
        method: "POST",
        body: JSON.stringify({
          account_id: account_id,
          amount: parseInt(amount),
        }),
        headers: {
          'Content-type': 'application/json',
        },
      });
      let resJsonPost = await res.json();
      if (res.status === 201) {
        try {
          // Get all transactions
          let res_get_trans = await fetch("http://127.0.0.1:5000/api/v1/transactions", {
            method: "GET",
            headers: {
              'Content-type': 'application/json',
            },
          });
          let resJsonGetTrans = await res_get_trans.json();
          if (res_get_trans.status === 200) {
            setHistory(resJsonGetTrans);
          }
          // Get account info
          let res_get_account = await fetch(`http://127.0.0.1:5000/api/v1/accounts/${account_id}`, {
            method: "GET",
            headers: {
              'Content-type': 'application/json',
            },
          });
          let resJsonGetAccount = await res_get_account.json();
          if (res_get_trans.status === 200) {
            if (amount >= 0) {
              setSummary(`Transferred ${amount}$ to account ${account_id}`);
            } else {
              setSummary(`Transferred ${Math.abs(amount)}$ from account ${account_id}`);
            }
            setBalance(`The current account balance is ${resJsonGetAccount.balance}$`);
          }
        } catch (err) {
          console.log(err);
        }
        setAccountID("");
        setAmount("");
        setMessage("Transaction created successfully");
      } else {
        setMessage(`${res.statusText}`);
      }
    } catch (err) {
      console.log(err);
    }
  };

  return (
    <div className="App">
      <div className="column">
        <form onSubmit={handleSubmit} className="submit-transaction">
          <label><h2>Submit new transaction</h2></label>
          <p>
            <input
              type="text"
              value={account_id}
              placeholder="Account ID(UUID)"
              onChange={(e) => setAccountID(e.target.value)}
            />
            <input
              type="number"
              value={amount}
              placeholder="Amount"
              onChange={(e) => setAmount(e.target.value)}
            />
            <button type="submit">Submit</button>
          </p>
          <p className="message">{message ? <p>{message}</p> : null}</p>
        </form>
      </div>
      <div className="column">
        <label><h2>Transaction history</h2></label>
        <List>
          <ListItem>
            {summary ? <p className="summary">{summary}<p className="balance">{balance}</p></p> : null}
          </ListItem>
          {history ? <p className="history">{
            history.map(home => <div><ListItem>Transferred {home.amount}$ to account {home.account_id}</ListItem></div>)
          }</p> : null}
        </List>
      </div>
    </div >
  );
};


export default PostTransactions;
