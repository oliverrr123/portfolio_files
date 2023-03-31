% include('header.tpl', title='Nabídka statistik')
<h2>Zabití za zápas</h2>
<div class="list">
<ul>
%for mode in modes:
  <li><a href="/kpm/{{mode}}">{{mode}}</a></li>    
%end
</ul>
</div>
% include('footer.tpl')