const { app, BrowserWindow } = require('electron');
const { exec } = require('child_process');
const basePythonPath = '../python/python-exe';
const path = require('path');
const url = require('url');
const startUrl =
	process.env.ELECTRON_START_URL ||
	url.format({
		pathname: path.join(__dirname, '/../build/index.html'),
		protocol: 'file:',
		slashes: true
	});

var window;

//-- MAD PROPS DMzda --//
/* let pyExec = exec(
	'cd ./src/python && pipenv install && pipenv run python main.py'
);

pyExec.stdout.on('data', data => {
	// Parse json string
	try {
		json = JSON.parse(data.toString());

		if (json.error !== null) {
			console.log(`${json.error.type} (${json.conf}): ${json.error.message}`);
			return;
		}

		if (json.predict !== null) {
			console.log(`Prediction (${json.conf}): ${json.predict}`);
		}
	} catch (error) {
		console.log(`[main.js (catch-block)]: ${data.toString()}`);
	}
});

pyExec.stderr.on('data', data => {
	console.log(data.toString());
}); */

// The main.js should create windows and handle all the system events your application might encounter
const createWindow = () => {
	window = new BrowserWindow({ width: 800, height: 600 });
	window.loadURL(startUrl);
	window.webContents.openDevTools();

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
