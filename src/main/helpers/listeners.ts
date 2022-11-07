import { ipcMain } from 'electron';
import { spawn } from 'child_process'
import { IPCActions } from '../../helpers/types'

// Helpers
const logParser = async (input: Buffer): Promise<any> => {
    return new Promise(resolve => {
        try {
            const payload = JSON.parse(input.toString())
            resolve(payload)
        } catch (error) {
            console.log('Not json object -- just printing')
            console.log(`${input}`)
        }
    })
}

// Setup ipc listeners
const spawnListeners = () => {
    ipcMain.on(IPCActions.startCapturing, async (event, arg) => {
        console.log('Spawning python script')
        const python = spawn('./python/venv/Scripts/python.exe', ['./python/ocr.py'])

        python.stdout.on('data', async data => {
            // If we return a json object, we can use that here else just print
            const payload = await logParser(data)

            if (payload) {
               event.sender.send(IPCActions.startCapturingReply, payload)
            }
        })
      
        python.stderr.on('data', data => {
            if (data) {
                console.log(`ERROR: ${data}`)
            }
        })
      
        python.on('close', code => {
            console.log(`SPAWN CLOSED: ${code}`)
        })
    })
}

export { spawnListeners, IPCActions }