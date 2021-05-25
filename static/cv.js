
 let txt='Hi, Welcome to my cv website, Please contact me with Whatsapp';
 let i=0;
 let anna="Anna Pertzovski";
 let phone="0547252304"
let myEmail= "pertzovski.anna@gmail.com"

console.log(txt)
function WelcomeText() {
    if (i<txt.length ){}
    {
        document.getElementById("myWelcome").innerHTML += txt.charAt(i);
        i++;
        setTimeout(WelcomeText,20);
    }
}
 function Buttonsanna () {
     document.getElementById("Anna_Pertzovski").innerHTML= anna;
 }

 function Buttonsphone () {
     document.getElementById("phone").innerHTML= phone;
 }

 function Buttonsemail () {
     document.getElementById("myemail").innerHTML= myEmail;
 }


function goTolist(){

  fetch('https://reqres.in/api/users?page=2')
      .then(response => response.json())
      .then(users => {
        let output = '<h2> People List</h2>';
        output += '<ul>';
        users.data.map(user =>
        {
          output += `
                            <li>
                                ${user.first_name} ${user.last_name} ${user.email}
                            </li>
                        `;
        });
        output += '</ul>'
      document.getElementById("response").innerHTML = output;
        let show = document.getElementById("list");
        show.style.display='block';
      });
}



