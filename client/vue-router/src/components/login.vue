/* eslint-disable */
<template>
  <div id="login" class='container'>
    <div class="container-fluid">
    <center>
      <img src="../assets/Book.png" width="80%" />
      <h1 class="text-dark font-weight-bold">{{ msg }}</h1>
    </center>
    </div>
    <br>
    <div class="container-fluid">
      <center>
        <div class="middle">
          <div id="logindiv">
            <form action="javascript:void(0);" method="get">
              <fieldset class="clearfix">
                <p>
                  <span class="fa fa-user"></span>
                  <input type="text" placeholder="Username" ref="username" required />
                </p>
                <!-- JS because of IE support; better: placeholder="Username" -->
                <p>
                  <span class="fa fa-lock"></span>
                  <input type="password" placeholder="Password" ref="password" required />
                </p>
                <!-- JS because of IE support; better: placeholder="Password" -->

                <div>
                  <span style="width:48%; text-align:left;  display: inline-block;">
                    <a class="text-dark" :to="{name: 'forget-password'}">
                      Forgot
                      password?
                    </a>
                  </span>
                  <span style="width:50%; text-align:right;  display: inline-block;">
                    <i class="fa fa-sign-in"></i> <input type="submit" value="Sign In" @click.prevent="getToken()" />
                  </span>
                </div>
              </fieldset>
              <div class="clearfix"></div>
            </form>

            <div class="clearfix"></div>
          </div>
          <!-- end login -->
          <div class="logo">
            <img src="../assets/logoside.png" width="50%" />
            <div class="clearfix"></div>
          </div>
        </div>
      </center>
    </div>
  </div>
</template>

<script>
import axios from "axios";
import router from '../router';
export default {
  name: "login",
  data() {
    return {
      msg: "Login Here!"
    }
  },
  methods: {
    getToken() {
      this.username = this.$refs.username.value;
      this.password = this.$refs.password.value;
      console.log(this.username);
      var bodyFormData = new FormData();
      bodyFormData.set("username", this.username);
      bodyFormData.set("password", this.password);
      axios({
        method: "post",
        url: "http://127.0.0.1:8000/auth/token/login/",
        data: bodyFormData,
        headers: { "Content-Type": "multipart/form-data" }
      })
        .then(function(response) {
          //handle success
          console.log(response);
          if (response.status === 200 && 'auth_token' in response.data) {
              localStorage.setItem('auth_token', response.data.auth_token)
            //   this.$session.start()
            //   this.$session.set('auth_token', response.data.auth_token)
            //   Vue.http.headers.common['Authorization'] = 'Bearer ' + response.data.auth_token
              router.push('/profile')
          }
            },
            function (err) {
            console.log('err', err)
        })
        .catch(function(response) {
          //handle error
          console.log(response);
        });
    }
  }
};
</script>
<style scoped>
[class*="fontawesome-"]:before {
  font-family: 'FontAwesome', sans-serif;
}

/* ---------- GENERAL ---------- */

/* * {
  box-sizing: border-box;
    margin:0px auto;

  &:before,
  &:after {
    box-sizing: border-box;
  }

} */

body {

    color: #606468;
  font: 87.5%/1.5em 'Open Sans', sans-serif;
  margin: 0;
}

a {
	color: #eee;
	text-decoration: none;
}

a:hover {
	text-decoration: underline;
}

input {
	border: none;
	font-family: 'Open Sans', Arial, sans-serif;
	font-size: 14px;
	line-height: 1.5em;
	padding: 0;
	-webkit-appearance: none;
}

p {
	line-height: 1.5em;
}

.clearfix {
  *zoom: 1;

  &:before,
  &:after {
    content: ' ';
    display: table;
  }

  &:after {
    clear: both;
  }

}

.container {
  left: 50%;
  position: fixed;
  top: 50%;
  transform: translate(-50%, -50%);
}

/* ---------- LOGIN ---------- */

#login form{
	width: 250px;
}
#login, .logo{
    display:inline-block;
    width:40%;
}
#logindiv{
border-right:1px solid rgb(0, 0, 0);
  padding: 0px 22px;
  width: 59%;
}
/* .logo{
color:#fff;
font-size:50px;
  line-height: 125px;
} */

#login form span.fa {
	background-color: #fff;
	border-radius: 3px 0px 0px 3px;
	color: #000;
	display: block;
	float: left;
	height: 50px;
    font-size:24px;
	line-height: 50px;
	text-align: center;
	width: 50px;
}

#login form input {
	height: 50px;
}
fieldset{
    padding:0;
    border:0;
    margin: 0;

}
#login form input[type="text"], input[type="password"] {
	background-color: #fff;
	border-radius: 0px 3px 3px 0px;
	color: #000;
	margin-bottom: 1em;
	padding: 0 16px;
	width: 200px;
}

#login form input[type="submit"] {
  border-radius: 3px;
  -moz-border-radius: 3px;
  -webkit-border-radius: 3px;
  background-color: #000000;
  color: #eee;
  font-weight: bold;
  /* margin-bottom: 2em; */
  text-transform: uppercase;
  padding: 5px 10px;
  height: 30px;
}

#login form input[type="submit"]:hover {
	background-color: #d44179;
}

#login > p {
	text-align: center;
}

#login > p span {
	padding-left: 5px;
}
.middle {
  display: flex;
  width: 600px;
}
</style>