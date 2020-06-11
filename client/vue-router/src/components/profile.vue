/* eslint-disable */
<template>
    <div id="profile" class='container-fluid'>
        <div class="row">
            <div class="col col-sm">

                <div class="card hovercard">
                    <div class="cardheader">

                    </div>
                    <div class="avatar">
                        <img alt="" src="data:image/png;base64,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">
                    </div>
                    <div class="info">
                        <div class="title">
                            {{username}}
                        </div>
                        <div class="desc">
                            {{email}}</div>
                    </div>
                    <div class="bottom">
                        <a class="btn btn-primary btn-twitter btn-sm" href="https://twitter.com/webmaniac">
                            <i class="fa fa-twitter"></i>
                        </a>
                        <a class="btn btn-danger btn-sm" rel="publisher"
                        href="https://plus.google.com/+ahmshahnuralam">
                            <i class="fa fa-google-plus"></i>
                        </a>
                        <a class="btn btn-primary btn-sm" rel="publisher"
                        href="https://plus.google.com/shahnuralam">
                            <i class="fa fa-facebook"></i>
                        </a>
                        <a class="btn btn-warning btn-sm" rel="publisher" href="https://plus.google.com/shahnuralam">
                            <i class="fa fa-behance"></i>
                        </a>
                    </div>
                </div>
            </div>
        </div>
        <div class='container'>
            <div class='row'>
                <div class="col-lg-4 col-sm-6">
                    <div class="card" style="width: 18rem;">
                        <img class="card-img-top" src="../assets/book_white.png" alt="Card image cap">
                        <div class="card-body dark">
                            <h5 class="card-title">Book</h5>
                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                            <a href="#" class="btn btn-dark">Go somewhere</a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-sm-6">
                    <div class="card" style="width: 18rem;">
                        <img class="card-img-top" src="../assets/book_black.png" alt="Card image cap">
                        <div class="card-body">
                            <h5 class="card-title">Book</h5>
                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                            <a href="#" class="btn btn-dark">Go somewhere</a>
                        </div>
                    </div>
                </div>
                <div class="col-lg-4 col-sm-6">
                    <div class="card" style="width: 18rem;">
                        <img class="card-img-top" src="../assets/book_white.png" alt="Card image cap">
                        <div class="card-body">
                            <h5 class="card-title">Book</h5>
                            <p class="card-text">Some quick example text to build on the card title and make up the bulk of the card's content.</p>
                            <a href="#" class="btn btn-dark">Go somewhere</a>
                        </div>
                    </div>
                </div>
        </div>
        </div>
    </div>
</template>
<script>
import axios from "axios";
export default {
  name: 'profile',
    data () {
    return {
      info: null,
      username: null,
      email : null,
    }
  },
  mounted () {
      var token=localStorage.getItem('auth_token')
     axios({
        method: "get",
        url: "http://127.0.0.1:8000/auth/users/me/",
        headers: { 'Authorization': 'Token '+token }
      })
       .then(response=> {
          //handle success
          this.username=response.data.username
          this.id=response.data.id
          this.email=response.data.email
       })
  }
}
</script>
<style scoped>
.card {
    padding-top: 20px;
    margin: 10px 0 20px 0;
    background-color: rgba(214, 224, 226, 0.2);
    border-top-width: 0;
    border-bottom-width: 2px;
    -webkit-border-radius: 3px;
    -moz-border-radius: 3px;
    border-radius: 3px;
    -webkit-box-shadow: none;
    -moz-box-shadow: none;
    box-shadow: none;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
}

.card .card-heading {
    padding: 0 20px;
    margin: 0;
}

.card .card-heading.simple {
    font-size: 20px;
    font-weight: 300;
    color: #777;
    border-bottom: 1px solid #e5e5e5;
}

.card .card-heading.image img {
    display: inline-block;
    width: 46px;
    height: 100px;
    margin-right: 15px;
    vertical-align: top;
    border: 0;
    -webkit-border-radius: 50%;
    -moz-border-radius: 50%;
    border-radius: 50%;
}

.card .card-heading.image .card-heading-header {
    display: inline-block;
    vertical-align: top;
}

.card .card-heading.image .card-heading-header h3 {
    margin: 0;
    font-size: 14px;
    line-height: 16px;
    color: #262626;
}

.card .card-heading.image .card-heading-header span {
    font-size: 12px;
    color: #999999;
}

.card .card-body {
    padding: 0 20px;
    margin-top: 20px;
}

.card .card-media {
    padding: 0 20px;
    margin: 0 -14px;
}

.card .card-media img {
    max-width: 100%;
    max-height: 100%;
}

.card .card-actions {
    min-height: 30px;
    padding: 0 20px 20px 20px;
    margin: 20px 0 0 0;
}

.card .card-comments {
    padding: 20px;
    margin: 0;
    background-color: #f8f8f8;
}

.card .card-comments .comments-collapse-toggle {
    padding: 0;
    margin: 0 20px 12px 20px;
}

.card .card-comments .comments-collapse-toggle a,
.card .card-comments .comments-collapse-toggle span {
    padding-right: 5px;
    overflow: hidden;
    font-size: 12px;
    color: #999;
    text-overflow: ellipsis;
    white-space: nowrap;
}

.card-comments .media-heading {
    font-size: 13px;
    font-weight: bold;
}

.card.people {
    position: relative;
    display: inline-block;
    width: 170px;
    height: 300px;
    padding-top: 0;
    margin-left: 20px;
    overflow: hidden;
    vertical-align: top;
}

.card.people:first-child {
    margin-left: 0;
}

.card.people .card-top {
    position: absolute;
    top: 0;
    left: 0;
    display: inline-block;
    width: 170px;
    height: 150px;
    background-color: #ffffff;
}

.card.people .card-top.green {
    background-color: #53a93f;
}

.card.people .card-top.blue {
    background-color: #427fed;
}

.card.people .card-info {
    position: absolute;
    top: 150px;
    display: inline-block;
    width: 100%;
    height: 101px;
    overflow: hidden;
    background: #ffffff;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
}

.card.people .card-info .title {
    display: block;
    margin: 8px 14px 0 14px;
    overflow: hidden;
    font-size: 16px;
    font-weight: bold;
    line-height: 18px;
    color: #404040;
}

.card.people .card-info .desc {
    display: block;
    margin: 8px 14px 0 14px;
    overflow: hidden;
    font-size: 12px;
    line-height: 16px;
    color: #737373;
    text-overflow: ellipsis;
}

.card.people .card-bottom {
    position: absolute;
    bottom: 0;
    left: 0;
    display: inline-block;
    width: 100%;
    padding: 10px 20px;
    line-height: 29px;
    text-align: center;
    -webkit-box-sizing: border-box;
    -moz-box-sizing: border-box;
    box-sizing: border-box;
}

.card.hovercard {
    position: relative;
    padding-top: 0;
    overflow: hidden;
    text-align: center;
    background-color: rgba(214, 224, 226, 0.2);
}

.card.hovercard .cardheader {
    background: url("http://lorempixel.com/850/280/nature/4/");
    background-size: cover;
    height: 135px;
}

.card.hovercard .avatar {
    position: relative;
    top: -50px;
    margin-bottom: -50px;
}

.card.hovercard .avatar img {
    width: 150px;
    height: 150px;
    max-width: 150px;
    max-height: 150px;
    -webkit-border-radius: 50%;
    -moz-border-radius: 50%;
    border-radius: 50%;
    border: 5px solid rgba(255,255,255,0.5);
}

.card.hovercard .info {
    padding: 4px 8px 10px;
}

.card.hovercard .info .title {
    margin-bottom: 4px;
    font-size: 24px;
    line-height: 1;
    color: #262626;
    vertical-align: middle;
}

.card.hovercard .info .desc {
    overflow: hidden;
    font-size: 12px;
    line-height: 20px;
    color: #737373;
    text-overflow: ellipsis;
}

.card.hovercard .bottom {
    padding: 0 20px;
    margin-bottom: 17px;
}

/* .btn{ border-radius: 50%; width:32px; height:32px; line-height:18px;  } */

</style>