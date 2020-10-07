<html>
    <head>
        <title>Thanks</title>

<meta name="viewport" content="width=device-width, initial-scale=1">
<style>
table, th, td {
  border: 1px solid black;
  border-collapse: collapse;
}
table.center {
  margin-left:auto;
  margin-right:auto;
}
</style>
    </head>
    <body>
    <pre style="text-align:center">

Dear Professor, Greeting from <b> Saifuddin Mahmud</b>. I am very lucky to be a student of this
course. I am also greatful to you as you are doing a great job for us. I never get a chance to work
       in the industry but I am feeling now. <b>This web application is for Homework 1.</b>


      </pre>
      <p style="text-align:center">Symptoms of COVID-19

<table  border="1" class="center" >
%for row in rows:
    <tr>
    %for item in row:
        <td>{{item}}</td>
    %end
    </tr>
%end
</table>
<a href="/new_symtoms">New Symtoms...</a>
</p>
    </body>
</html>