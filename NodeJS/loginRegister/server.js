import express from "express";
import dotenv from 'dotenv';
import cors from 'cors';

const app = express(); //initialize express
app.use(cors());

//from body parser
app.use(express.urlencoded({extended:true}));
app.use(express.json());

dotenv.config();

//listen the server
app.listen(process.env.PORT || 3001, () => {
    console.log(`run on ${process.env.PORT || 3001}`);
})