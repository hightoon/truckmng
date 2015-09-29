<div class="panel panel-danger">
  <!-- Default panel contents -->
  <div class="panel-heading">最近违章记录</div>
  <div class="panel-body">
    <p>最近30条违章记录</p>
  </div>

  <!-- Table -->
  <table class="table">
	<thead>
		<tr>
		  %for col in results[0]:
		    <th>{{col}}</th>
		  %end
		</tr>
	</thead>
	<tbody>
		%for res in results[1:]:
		  <tr>
		  %for col in res:
		    <td>{{col}}</td>
		  %end
		  </tr>
		%end
	</tbody>
  </table>
</div>