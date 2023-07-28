const robots = [
    {
      id: 1,
      name: 'Leanne Graham',
      username: 'Bret',
      email: 'Sincere@april.biz',
      image: 'https://robohash.org/1?200x200'
    },
    {
      id: 2,
      name: 'Ervin Howell',
      username: 'Antonette',
      email: 'Shanna@melissa.tv',
      image: 'https://robohash.org/2?200x200'
    },
    {
      id: 3,
      name: 'Clementine Bauch',
      username: 'Samantha',
      email: 'Nathan@yesenia.net',
      image: 'https://robohash.org/3?200x200'
    },
    {
      id: 4,
      name: 'Patricia Lebsack',
      username: 'Karianne',
      email: 'Julianne.OConner@kory.org',
      image: 'https://robohash.org/4?200x200'
    },
    {
      id: 5,
      name: 'Chelsey Dietrich',
      username: 'Kamren',
      email: 'Lucio_Hettinger@annie.ca',
      image: 'https://robohash.org/5?200x200'
    },
    {
      id: 6,
      name: 'Mrs. Dennis Schulist',
      username: 'Leopoldo_Corkery',
      email: 'Karley_Dach@jasper.info',
      image: 'https://robohash.org/6?200x200'
    },
    {
      id: 7,
      name: 'Kurtis Weissnat',
      username: 'Elwyn.Skiles',
      email: 'Telly.Hoeger@billy.biz',
      image: 'https://robohash.org/7?200x200'
    },
    {
      id: 8,
      name: 'Nicholas Runolfsdottir V',
      username: 'Maxime_Nienow',
      email: 'Sherwood@rosamond.me',
      image: 'https://robohash.org/8?200x200'
    },
    {
      id: 9,
      name: 'Glenna Reichert',
      username: 'Delphine',
      email: 'Chaim_McDermott@dana.io',
      image:'https://robohash.org/9?200x200'
    },
    {
      id: 10,
      name: 'Clementina DuBuque',
      username: 'Moriah.Stanton',
      email: 'Rey.Padberg@karina.biz',
      image:'https://robohash.org/10?200x200'
    }
    ];
const mainDiv = document.getElementById('container');
const message = document.getElementById('message');

function createRobots(robotArray){
    robotArray.forEach((element,index) => {
        const cardDiv = document.createElement('div');
        const imgDiv = document.createElement('img');
        imgDiv.setAttribute("src", element["image"]);
        const contDiv = document.createElement('div');
        const textHead = document.createElement('h4');
        const newTextName = document.createTextNode(element["name"]);
        const textP = document.createElement('p');
        const newTextP = document.createTextNode(element["email"]);
    
        cardDiv.classList.add('card');
        contDiv.classList.add('content');
        
        contDiv.append(textHead, textP);
        textHead.appendChild(newTextName);
        textP.appendChild(newTextP);
        cardDiv.append(imgDiv, contDiv);
        mainDiv.appendChild(cardDiv);
    })
}
createRobots(robots);

function myFilter() {
    mainDiv.innerHTML = "";
    let input = document.getElementById("myInput");
    let searchInput = input.value.toUpperCase();
    let newArray=robots.filter((robot)=> robot.name.toUpperCase().includes(searchInput));
    createRobots(newArray);
    if (newArray.length === 0) {
        message.innerText = "Sorry, No robots found!";
    } else {
        message.innerText = "";
    }
}
