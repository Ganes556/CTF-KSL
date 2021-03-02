const express = require('express');
const bodyParser = require('body-parser');
const cookieParser = require('cookie-parser');
const flash = require('express-flash');
const mongoose = require('mongoose');
const LocalStrategy = require('passport-local').Strategy;
const path = require('path');
const passport = require('passport');
const session = require('express-session');
const router = require('./routers');

// init var
const app = express();

// mongodb
// mongoose.connect('SENSOR GAN');
// const db = mongoose.connection;

// views
app.set('views', path.join(__dirname, 'views'));
app.set('view engine', 'pug');

// express config
app.use(bodyParser.urlencoded({ extended: false }));
app.use(bodyParser.json());
app.use(cookieParser());
app.use(flash());
// app.use(session('SENSOR GAN'));


// passport
const { User } = require('./models');
app.use(passport.initialize());
app.use(passport.session());
passport.use(new LocalStrategy(User.authenticate()));
passport.serializeUser(User.serializeUser());
passport.deserializeUser(User.deserializeUser());

// Public folder
app.use(express.static(path.join(__dirname, 'public')));

// router
app.use(router.homeRouter);
app.use(router.userRouter);

app.listen(80, () => console.log('Server is Running!'));
