import { useEffect, useCallback } from 'react'
import { Button, VStack, Text } from '@chakra-ui/react';
import { IPCActions } from '../../helpers/types'



const Home = () => {
    
    // Actions
    const startCapturing = useCallback(async () => {
        window.electronAPI.startCapturing();
    }, [])

    const startCapturingReply = useCallback(() => {
        window.electronAPI.receive(IPCActions.startCapturingReply, (event: any, result: any) => {
            console.log('receiving payload...')
            console.log(result.pop())
        })
    }, [])
    
    
    useEffect(() => {
        startCapturingReply()
    }, [])

    return (<VStack bgColor="green.300" h="100vh">
        <VStack bg="blue.300" h="100%">        
            <Text fontSize="2xl">Welcome to HypeVision.</Text>
            <Text fontSize="xl">Click the the button below to get started.</Text>
            <Button onClick={startCapturing}>Click to start capturing</Button>
        </VStack>
    </VStack>);
};

export default Home