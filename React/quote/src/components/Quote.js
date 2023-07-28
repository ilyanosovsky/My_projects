import { useEffect, useState } from "react";
import quotes from "./QuoteData";

const Quote = () => {

    const [quoteData, setQuoteData] = useState({
        quote: "",
        author: "",
        index: quotes.length + 1,
      });

    useEffect(() => {
        handleClick();
    }, []);


    const handleClick = () => {

        let randomNumber;
        do {
          randomNumber = Math.floor(Math.random() * quotes.length);
        } while (randomNumber === quoteData.index);

        let randomColor = `#${Math.floor(Math.random() * 16777215).toString(16)}`;
        document.body.style.backgroundColor = randomColor;
    
        let item = quotes[randomNumber];
    
        setQuoteData({
          quote: item.quote,
          author: item.author,
          index: randomNumber,
        });
    };


    const author = quoteData.author.length > 0 ? quoteData.author : "Unknown";


    return(
        <div style={{
            display:'inline-block',
            padding: '20px',
            margin: '20px',
            border: '1px solid white',
            backgroundColor: 'grey',
            borderRadius: '20px'
        }}>
          <div>
              <h1>"{quoteData.quote}"</h1>
              <p><i>-{author}-</i></p>
          </div>
            <button onClick={handleClick} style={{
                                color: 'black', 
                                backgroundColor: 'white', 
                                padding: '5px 10px', 
                                border: '1px solid white', 
                                borderRadius: '36px'
                                }}>New quote</button>
        </div>
    )
}

export default Quote;