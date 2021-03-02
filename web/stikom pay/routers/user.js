const connectEnsureLogin = require('connect-ensure-login');
const express = require('express');
const passport = require('passport');
const userRouter = express.Router();
const { User, Transaction } = require('../models');
const { visit } = require('../utils');

userRouter.get('/login', 
	connectEnsureLogin.ensureLoggedOut(),
	(_, res) => res.render('login')
);
userRouter.get('/register', 
	connectEnsureLogin.ensureLoggedOut(),
	(_, res) => res.render('register')
);
userRouter.get('/profile',
	connectEnsureLogin.ensureLoggedIn(),
	async (req, res) => {
		const transactions = await Transaction
			.find({
				$or: [
					{ from: req.user._id },
					{ to: req.user._id }
				]
			})
			.populate('to')
			.populate('from')
			.sort([ ['date', -1] ])
			.limit(2);

		res.render('profile', {
			transactions,
			title: 'Profile | Stikom Pay'
		});
	}
);
userRouter.get('/gantinama',
	connectEnsureLogin.ensureLoggedIn(),
	(_, res) => res.render('gantinama')
);
userRouter.post('/gantinama',
	connectEnsureLogin.ensureLoggedIn(),
	async (req, res) => {
		try {
			await User.findOneAndUpdate({ username: req.user.username }, { name: req.body.name });

			req.flash('success', 'Nama berhasil diganti.');
			return res.redirect('/profile');
		} catch(e) {
			req.flash('error', e.message);
			return redirect('/gantinama')
		}
	}
);

userRouter.post('/login', 
	connectEnsureLogin.ensureLoggedOut(),
	passport.authenticate('local', {
		successRedirect: '/profile',
		failureRedirect: '/login',
		failureFlash: true,
	})
);

userRouter.post('/register', (req, res) => {
	const { name, username, password } = req.body;
	const newUser = new User({ name, username });

	User.register(newUser, password, function (err) {
		if (err) {
			req.flash('error', err.message);
			res.status(400).redirect('/register');
		}

		passport.authenticate('local')(req, res, function () {
			return res.redirect('/profile');
		});
	});
});

userRouter.get('/logout',
	connectEnsureLogin.ensureLoggedIn(),
	(req, res) => {
		req.session.destroy();
		req.logout();
		return res.redirect('/');
	}
);

userRouter.post('/sendcoins',
	connectEnsureLogin.ensureLoggedIn(),
	async (req, res) => {
		const { target, coins } = req.body;

		if (coins <= 0) {
			req.flash('error', 'Minimal transaksi 1 coins');
			return res.redirect('/profile');
		}
		if (coins > 1000) {
			req.flash('error', 'Transaksi yang anda lakukan melebihi batas maksimum!');
			return res.redirect('/profile');
		}
		if (req.user.coins < coins) {
			req.flash('error', 'Coin tidak cukup untuk melakukan transaksi');
			return res.redirect('/profile');
		}

		try {
			const newTransaction = new Transaction({
				from: req.user._id,
				to: (await User.findOne({ username: target }).orFail())._id,
				amount: coins
			});
			const updateTargetUser = await User
				.findOneAndUpdate({ username: target }, {
					$inc:{ coins }
				});
			const updateCurrentUser = await User
				.findOneAndUpdate({ username: req.user.username }, {
					$inc: { coins: -coins }
				});

			await newTransaction.save();
			await updateTargetUser.save();
			await updateCurrentUser.save();

			// admin visiting his profile
			target === 'admin' && await visit();

			req.flash('success', 'Transaction Success!');
			return res.redirect('/profile');
		} catch (e) {
			req.flash('error', e.message);
			return res.redirect('/profile');
		}
	}
);

module.exports = userRouter;
