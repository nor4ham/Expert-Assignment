import { useState, useEffect } from "react";
import axios from "axios";
import CurrencyInput from './CurrencyInput'
import Result from './Result'
import format from "date-fns/format"
export default function Converter() {
  const [amount1, setAmount1] = useState(1);
  const [amount2, setAmount2] = useState(1);
  const [currency1, setCurrency1] = useState('USD');
  const [currency2, setCurrency2] = useState('SAR');
  const [rates, setRates] = useState([]);
  function handleAmount1Change(amount1) {
    setAmount2(format(amount1 * rates[currency2] / rates[currency1]));
    setAmount1(amount1);
  }
  function handleCurrency1Change(currency1) {
    setAmount2(format(amount1 * rates[currency2] / rates[currency1]));
    setCurrency1(currency1);
  }



  function handleAmount2Change(amount2) {
    setAmount1(format(amount2 * rates[currency1] / rates[currency2]));
    setAmount2(amount2);
  }
  function handleCurrency2Change(currency2) {
    setAmount1(format(amount2 * rates[currency1] / rates[currency2]));
    setCurrency2(currency2);
  }


 

/*   let myHeaders = new Headers();
  myHeaders.append("apikey", "Z9eT0bJ33HUJb52uMA9O53tvTCboKyj5");

  let requestOptions = {
  method: 'GET',
  redirect: 'follow',
  headers: myHeaders};

 */
  useEffect(() => {
    /*    
    fetch("https://api.apilayer.com/fixer/latest?base=USD", requestOptions)
    .then(response => response.text())
    .then(result => console.log("hi",result))
    .catch(error => console.log('error', error));
*/
 axios.get('https://api.apilayer.com/fixer/latest?base=USD&apikey=Z9eT0bJ33HUJb52uMA9O53tvTCboKyj5')
      .then(response => {
        setRates(response.data.rates);
      }) 
  }, []);

  return (
    <div className='container'>
      <CurrencyInput
        amount={amount1}
        currency={currency1}
        currencies={Object.keys(rates)} 
        onAmountChange={handleAmount1Change}
        onCurrencyChange={handleCurrency1Change}

      />
      <CurrencyInput
         amount={amount2}
         currency={currency2}  
         currencies={Object.keys(rates)}
         onAmountChange={handleAmount2Change}
         onCurrencyChange={handleCurrency2Change}
      />
      <Result/>
  </div>
  )
}
