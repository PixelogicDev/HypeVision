import { contextBridge, ipcRenderer } from 'electron';
import { IPCActions } from '../helpers/types'

contextBridge.exposeInMainWorld('electronAPI', {
    startCapturing: () => ipcRenderer.send(IPCActions.startCapturing),
    receive: (channel: string, func: any) => ipcRenderer.on(
        channel,
        (event, ...args) => func(event, args)
    )
})
