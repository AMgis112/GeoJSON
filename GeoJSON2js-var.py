// python script to convert geojson to javascript variable
// https://www.w3schools.com/python/python_file_write.asp
// var storing the javascript variable (ie var locations = )
// bring in geojson as string
// create a javascript file
// open a javascript file
// write the js variable
// write (or append) the geojson string
// save/close file

html_str = """
<table border=1>
     <tr>
       <th>Number</th>
       <th>Square</th>
     </tr>
     <indent>
     <% for i in range(10): %>
       <tr>
         <td><%= i %></td>
         <td><%= i**2 %></td>
       </tr>
     </indent>
</table>
"""

Html_file= open("filename","w")
Html_file.write(html_str)
Html_file.close()
