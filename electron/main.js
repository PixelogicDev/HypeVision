const { app, BrowserWindow } = require('electron');
const { exec } = require('child_process');
const basePythonPath = '../python/python-exe';

var window;
//-- MAD PROPS DMzda --//
exec(
	'cd ../python && pipenv install && pipenv run python main.py',
	(err, stdout, stderr) => {
		if (err) {
			console.log(err);
			return;
		}

		if (stderr) {
			console.log(stderr);
			return;
		}

		console.log(stdout);
	}
);

// The main.js should create windows and handle all the system events your application might encounter
const createWindow = () => {
	window = new BrowserWindow({ width: 800, height: 600 });
	window.loadURL('https://github.com/PixelogicDev/HypeVision');

	// Window event listeners //
	app.on('activate', () => {
		// On macOS it's common to re-create a window in the app when the
		// dock icon is clicked and there are no other windows open.
		if (window === null) createWindow();
	});

	// Quit when all windows are closed.
	app.on('window-all-closed', () => {
		// On macOS it is common for applications and their menu bar
		// to stay active until the user quits explicitly with Cmd + Q
		if (process.platform !== 'darwin') {
			app.quit();
		}
	});

	window.on('closed', () => {
		// Probably should do some cleanup / state management //
		window = null;
	});
};

app.on('ready', createWindow);
