% include('header.tpl', title='Zabití za zápas')
<div class="list">
%for itm in data:
  <div class="listitem">
    <div class="title">{{itm[0]}}</div>
    <div class="score">{{itm[1]}}</div>
  </div>
%end
</div>
% include('footer.tpl')