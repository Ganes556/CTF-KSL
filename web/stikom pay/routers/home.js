const homeRouter = require('express').Router();
const connectEnsureLogin = require('connect-ensure-login');
const { User } = require('../models');

homeRouter.get('*', (req, res, next) => {
	res.locals.isAuthenticated = req.isAuthenticated();
	res.locals.user = req.user;
	res.locals.errors = req.flash('error');
	res.locals.success = req.flash('success');
	next();
});

homeRouter.get('/', async (req, res) => {
	const users = await User.find({})
		.sort([['coins', -1]])
		.limit(10);

	return res.render('home', { users });
});

homeRouter.get('/buyflag',
	connectEnsureLogin.ensureLoggedIn(),
	async (req, res) => {
		if (parseInt(req.user.coins) >= 1000) {
			await User
				.findOneAndUpdate({ username: req.user.username }, {
					$inc: { coins: -1000 }
				});

			return res.send('flag nya disini gan');
		}

		req.flash('error', 'Coin tidak cukup!');
		return res.redirect('/profile')
	}
);

module.exports = homeRouter;
