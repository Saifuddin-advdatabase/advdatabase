<p>Todo List 1.1</p>
<table border="1">
%for row in rows:
    <tr>
    %for item in row:
        <td>{{item}}</td>
    %end
    </tr>
%end
</table>

<a href="/new_item">New Item...:=)</a>
<a href="/new_item">Update Item...:=)</a>
<a href="/new_item">Delete Item...:=)</a>
