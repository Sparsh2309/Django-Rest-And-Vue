/* eslint-disable */
<template>
  <div id="app">
    <!-- <img src="./assets/logo.png"> -->
    <!-- <nav class="navbar navbar-toggleable-sm navbar-trans navbar-inverse"> -->
  <nav class="navbar navbar-expand-lg navbar-toggleable-sm navbar-trans navbar-inverse cursive-font">
  <router-link class="navbar-brand text-dark cursive-font" to="/">
  <img src="./assets/Book.png" width='10%'></router-link>
  <button class="navbar-toggler" type="button" data-toggle="collapse" data-target="#navbarColor01" aria-controls="navbarColor01" aria-expanded="false" aria-label="Toggle navigation">
    <span class="navbar-toggler-icon"></span>
  </button>

  <div class="collapse navbar-collapse" id="navbarColor01">
    <ul class="navbar-nav mr-auto">
      <li class="nav-item active">
        <router-link class="nav-link text-dark cursive-font" to="/">Home</router-link>
      </li>
      <li class="nav-item">
        <router-link class="nav-link text-dark cursive-font" to="/blog">Blog</router-link>
      </li>
      <li class="nav-item">
        <a class="nav-link text-dark cursive-font" href="#">About</a>
      </li>
    </ul>
    <router-link class="btn btn-secondary my-2 my-sm-0 cursive-font" to="/login">Login</router-link>
    <router-link class="btn btn-secondary my-2 my-sm-0 cursive-font" to="/login">Log out</router-link>
  </div>
</nav>
  <router-view/>
  </div>
</template>

<script>
export default {
  name: 'App',
}
</script>

<style>

body {
  background-image: url('./assets/background.png');
  background-repeat:no-repeat;
  background-size:cover;
}
.cursive-font {
  font-family: "Bungee Shade", cursive;
}
a {
  color: #59a0d7; }

h1 {
  font-family: "Montserrat", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 4rem;
  font-weight: 600; }

h2 {
  font-family: "Montserrat", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 2.8rem;
  font-weight: 500; }

h3 {
  font-family: "Montserrat", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 2rem;
  font-weight: 500; }

h4 {
  font-family: "Montserrat", "Helvetica Neue", Helvetica, Arial, sans-serif;
  font-size: 1rem;
  font-weight: 700;
  text-transform: uppercase; }

p {
  color: #696b6e;
  font-size: .9rem; }

.divider {
  display: block;
  width: 6rem;
  height: 0.3rem;
  background-color: #dfe1e5;
  margin: 2rem auto; }

.navbar-trans {
  background: transparent; }

a.navbar-brand, a.logo {
  font-family: "Montserrat", "Helvetica Neue", Helvetica, Arial, sans-serif;
  color: #fff !important;
  font-size: 2rem;
  font-weight: bold;
  margin-top: 0; }

a.logo:hover, a.logo:active, a.logo:focus {
  text-decoration: none; }

li.nav-item .btn {
  margin-top: .2rem;
  margin-left: .4rem; }
li.nav-item .btn-white {
  color: #46484a; }

.cover {
  background: #2b2d34 url(./assets/background.png) center;
  background-size: cover;
  min-height: 50rem;
  height: auto;
  border-radius: 0;
  width: 100%;
  color: #fff;
  padding-top: 1rem; }

  .cover h1 {
    font-weight: 200; }

  .cover p.lead {
    margin: 2rem auto;
    color: rgba(255, 255, 255, 0.75); }

  .cover .cover-container {
    display: table;
    height: 100%;
    min-height: 44rem;
    margin: 0 auto; }

    .btn-primary, .btn-outline-primary, .btn-secondary, .btn-outline-secondary, .btn-white, .btn-outline-white, .btn-success, .btn-outline-success, .btn-info, .btn-outline-info, .btn-warning, .btn-outline-warning, .btn-danger, .btn-outline-danger {
  font-size: .75rem;
  text-transform: uppercase;
  font-weight: 700;
  border-radius: .3rem; }

.btn-outline-primary, .btn-outline-secondary, .btn-outline-white, .btn-outline-success, .btn-outline-info, .btn-outline-warning, .btn-outline-danger {
  border-width: 0.15rem; }

.btn-lg {
  padding: 1.1rem 2.5rem;
  font-size: .9rem; }

.btn-primary, .btn-primary:hover, .btn-primary:focus, .btn-primary:active {
  background-color: #59a0d7;
  border-color: #59a0d7; }

.btn-primary:hover, .btn-primary:focus, .btn-primary:active {
  background-color: #4089c1;
  border-color: #4089c1; }

.btn-outline-primary, .btn-outline-primary:visited {
  color: #59a0d7;
  border-color: #59a0d7;
  background: none; }

.btn-outline-primary:hover, .btn-outline-primary:focus, .btn-outline-primary:active {
  background-color: #59a0d7;
  border-color: #59a0d7;
  color: #fff; }

.btn-secondary {
  border-color: #696b6e;
  background-color: #696b6e;
  color: #fff; }

.btn-secondary:hover, .btn-secondary:focus, .btn-secondary:active {
  border-color: #46484a;
  background-color: #46484a;
  color: #fff; }

.btn-outline-secondary, .btn-outline-secondary:visited {
  color: #696b6e;
  border-color: #696b6e;
  background: none; }

.btn-outline-secondary:hover, .btn-outline-secondary:focus, .btn-outline-secondary:active {
  border-color: #696b6e;
  background: #696b6e;
  color: #fff; }

.btn-white {
  border-color: #fff;
  background-color: #fff;
  color: #46484a; }

.btn-white:hover, .btn-white:focus, .btn-white:active {
  border-color: #dfe1e5;
  background-color: #dfe1e5;
  color: #46484a; }

.btn-outline-white, .btn-outline-white:visited {
  background: none;
  color: #fff;
  border-color: #fff; }

.btn-outline-white:hover, .btn-outline-white:focus, .btn-outline-white:active {
  color: #46484a;
  background: #fff; }

.link-white, link-white:visited {
  font-size: .75rem;
  text-transform: uppercase;
  font-weight: 700;
  border-radius: .3rem;
  border: 0;
  color: #fff; }

.link-white:hover, .link-white:focus, .link-white:active {
  color: #dfe1e5 !important; }
</style>
