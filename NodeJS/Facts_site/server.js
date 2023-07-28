const express = require('express');
const cors = require("cors");
const bp = require('body-parser');
let Parser = require('rss-parser');
var path = require('path');
const ejs = require("ejs");
const app = express();


const url = 'https://thefactfile.org/feed/';

app.set('views', path.join(__dirname, '/public/pages'));
app.set('view engine', 'ejs');

app.use(cors());
app.use(express.static(__dirname + '/public'));
app.use(bp.urlencoded({extended:false}));
app.use(bp.json());

let parser = new Parser();


app.get('/', getFeed);
app.get('/search', getSearch);
app.post('/search/', postSearch );


async function getFeed(req, res)  {
    let feed = await parser.parseURL(url);
    res.render('index', feed);
};




async function getSearch(req, res) {
    let categories = [];
    let feed = await parser.parseURL(url);

    feed.items.forEach(item => {
        item.categories.forEach(category => {
            if (!categories.includes(category)) {
                categories.push(category);
            };
        });
    });
    res.render('search', {items: [], categories: categories});
};



async function postSearch (req, res) {
    let categories = [];
    let result = {items: [], categories: categories};
    let feed = await parser.parseURL(url);

    feed.items.forEach(item => {
        item.categories.forEach(category => {
            if (!categories.includes(category)) {
                categories.push(category);
            };
        });

        if ("searchTitle" in req.body) {
            if (item.title.includes(req.body.searchTitle) || item.content.includes(req.body.searchTitle)) {
                result.items.push(item);
            }
        } else if ("searchCategory" in req.body) {
            if (item.categories.includes(req.body.searchCategory)) {
                result.items.push(item);
            }
        }
    });
    res.render('search', result);
};



app.listen(process.env.PORT || 3001, ()=> {
console.log(`run in ${process.env.PORT || 3001}`); 
})