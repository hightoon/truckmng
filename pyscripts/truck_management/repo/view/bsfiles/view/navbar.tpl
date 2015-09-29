<nav class="navbar navbar-inverse navbar-fixed-top">
  <div class="container-fluid">
    <div class="navbar-header">
      <button type="button" class="navbar-toggle collapsed" data-toggle="collapse" data-target="#navbar" aria-expanded="false" aria-controls="navbar">
        <span class="sr-only">Toggle navigation</span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
        <span class="icon-bar"></span>
      </button>
      <a class="navbar-brand" href="/index">超限车辆查询管理系统</a>
    </div>
    <div id="navbar" class="navbar-collapse collapse">
      <ul class="nav navbar-nav navbar-right">
        <li><a href="#"><span class="glyphicon glyphicon-user" aria-hidden="true"></span> {{user}}</a></li>
        <!--li><a href="#">设置</a></li>
        <li><a href="/change_passwd">修改密码</a></li-->
        <li><a href="/logout"><span class="glyphicon glyphicon-off" aria-hidden="true"></span> 退出登录</a></li>
      </ul>
      <form class="navbar-form navbar-right">
        <input type="text" class="form-control" placeholder="搜索...">
      </form>
    </div>
  </div>
</nav>
