%include ('./view/bsfiles/view/html_hdr.tpl')

    <div class="container">

      <form class="form-signin" action="/login" method="POST">
        <h2 class="form-signin-heading">请登录信息管理系统</h2>
        <label for="inputEmail">用户名</label>
        <input type="text" id="inputEmail" name="usrname" class="form-control" placeholder="用户名" required autofocus>
        <label for="inputPassword">密码</label>
        <input type="password" id="inputPassword" name="passwd" class="form-control" placeholder="密码" required>
        <div class="checkbox">
          <label>
            <input type="checkbox" name="rememberme" value="remember-me"> 记住我
          </label>
        </div>
        <button class="btn btn-lg btn-primary btn-block" type="submit">登录</button>
      </form>

    </div> <!-- /container -->

%include ('./view/bsfiles/view/html_footer.tpl')
