import React, { Component } from 'react';
import './App.css';

//-- Components --//
import Input from './components/Input';

class App extends Component {
	constructor(props) {
		super(props);

		this.state = {
			inputs: [1]
		};
	}

	addInput = () => {
		this.setState(state => ({
			inputs: [...state.inputs, state.inputs.length + 1]
		}));
	};

	render() {
		return (
			<div className="App">
				{this.state.inputs.map((value, index) => (
					<Input key={index} />
				))}
				{/* Add Button to add more inputs */}
				<button onClick={() => this.addInput()}>Add Input</button>
			</div>
		);
	}
}

export default App;
