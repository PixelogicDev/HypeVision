

declare global {
  interface Window {
    electronAPI: {
      startCapturing(): void,
      receive(channel: string, func: any): void
    };
  }
}

export {};
