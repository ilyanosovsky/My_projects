// Note
// The program should take the currency which the user currently has and the currency in which 
// they would like to receive, as well as the amount of money. Afterwards, 
// the program will output the correct exchange rate based on the data from the APIs.

// First, you need to fetch all the supported currencies, in order to add the currencies 
// options (ie FROM - To) in the currency converter. Check out this page on Supported Codes Endpoint 
// from the ExchangeRate API documentation.

// To convert from a currency, to another one, you need to fetch conversion rate from 
// the Pair Conversion API endpoint. Check out this page on Pair conversion requests 
// from the ExchangeRate API documentation.
// Hint: You could also supply an optional AMOUNT variable in the query of the request.

// Bonus: Add this “switch” button on the page, when clicked on it will switch the currencies 
// and display the new amount converted.
// Example : if the conversion was from EUR to GBP, as soon as the button is clicked on, 
// the conversion should be from GBP to EUR.

// GET https://v6.exchangerate-api.com/v6/YOUR-API-KEY/codes
// GET https://v6.exchangerate-api.com/v6/YOUR-API-KEY/pair/EUR/GBP

let selectFrom = document.querySelector("#from");
let selectTo = document.querySelector("#to");
let amount = document.querySelector("#amount");
let output = document.querySelector("output");
const button = document.querySelector("#convert");


async function getCurrencies() {
    console.log("start fetching Currencies ...");
    try { 
        const response = await fetch(`https://v6.exchangerate-api.com/v6/a52cef8196b69478eb28f889/codes`)
        if(response.ok) {
            data = await response.json();
            console.log("data from API: ", data["supported_codes"]);
        } else {
            throw new Error ("issues with fetch")
        }
        return data["supported_codes"];
    } catch (error) {
        console.log("ERROR", error)
        return error
    }
}

// getCurrencies()


async function convert (convertFrom, convertTo, convertAmount) {
    console.log("start fetching Convert...");
    try { 
        const response = await fetch(`https://v6.exchangerate-api.com/v6/a52cef8196b69478eb28f889/pair/${convertFrom}/${convertTo}/${convertAmount}`)
        if(response.ok) {
            data = await response.json();
            console.log("Conversion result: ",data["conversion_result"]);
        } else {
            throw new Error ("issues with fetch")
        }
        return data["conversion_result"];
    } catch (error) {
        console.log("ERROR", error)
        return error
    }
}

// convert("NIO", "NAD", 100);

button.addEventListener("click", async function() {
    const amountToCheck = amount.value;
    const conversionResult = await convert(selectFrom.value, selectTo.value, amountToCheck);
    output.textContent = conversionResult;
});
  
async function getCurrenciesAndPopulateSelect() {
let currencies = await getCurrencies();

for (let currency of currencies) {
    let optionFrom = document.createElement("option");
    optionFrom.value = currency[0];
    optionFrom.textContent = `${currency[0]} - ${currency[1]}`;
    selectFrom.appendChild(optionFrom);

    let optionTo = document.createElement("option");
    optionTo.value = currency[0];
    optionTo.textContent = `${currency[0]} - ${currency[1]}`;
    selectTo.appendChild(optionTo);
    }
}

getCurrenciesAndPopulateSelect();