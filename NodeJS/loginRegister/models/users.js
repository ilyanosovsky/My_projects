import { db } from "../config/db.js";
import { hash } from "bcrypt";

export const register = ({first_name, last_name, username, email, created_date, last_login, hash}) => {
    db.transaction((trx) => { //controll the commit
        trx('users')
        .insert({first_name, last_name, username, email, created_date, last_login})
        .returning(['user_id', 'username', 'email', 'first_name', 'last_name'])

        .then(row => {
            return trx('login') //usong transactions avoid conflict with inserting into two tables
            .insert({
                username:row[0].username || username,  //it will be from DB or || from insert
                password: hash
            })
            .then((row) => {
                trx.commit;
            })
            .catch((err) => {
                trx.rollback;
            })
        })

        .then((row) => {
            trx.commit;
        })
        .catch((err) => {
            trx.rollback;
        });
    });
};

// do it the same but with ASYNC and AWAIT

// const register = async ({first_name, last_name, username, email, created_date, last_login, hash}) => {
//     try {
//         const res = await fetch('api/profile',{
//             method:'POST',
//             headers: {
//                 "content-type":"application/json"
//             },
//             body: JSON.stringify({first_name, last_name, username, email, created_date, last_login})
//             });

//             if (res.status === 200) {
//                 const data = await res.json();
//                 console.log(res);
//             } else {
//                 const data = await res.json();
//                 data.msg
//                 console.log("other status of resp:", data.msg);
//                 renderError(`Error ${res.status}: ${data.msg}`);
//             }
//     } catch (err) {
//         console.log("ERROR FROM SERVER:", err)
//     }
// }