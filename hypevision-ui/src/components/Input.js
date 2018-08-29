import React, { Component } from 'react';

class Input extends Component {
	constructor(props) {
		super(props);
		this.state = {
			ytLink: '',
			killCount: -1
		};
	}

	handleChange = event => {
		console.log(event.target.value);
		this.setState({
			[event.target.name]: event.target.value
		});
	};

	render() {
		//-- MAD PROPS KociQQ --//
		return [
			<input
				name="killCount"
				type="number"
				min="1"
				max="100"
				placeholder="Kill Count"
				onChange={this.handleChange}
				key="0"
			/>,
			<input
				name="ytLink"
				type="text"
				placeholder="YouTube Link"
				onChange={this.handleChange}
				key="1"
			/>
		];
	}
}

export default Input;
