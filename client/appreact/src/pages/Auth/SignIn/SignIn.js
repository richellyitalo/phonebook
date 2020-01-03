import React, { Component } from 'react';

import { Container, SignForm } from '../styles';
import Button from '../../../styles/components/Button';

export default class SignIn extends Component {
  state = {
    email: '',
    password: ''
  };

  handleSubmit = e => {
    e.preventDefault();

    const { email, password } = this.state;
  };

  handleInputChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  render() {
    const { email, password } = this.state;

    return (
      <Container>
        <SignForm onSubmit={this.handleSubmit}>
          <h1>Bem vindo</h1>

          <span>E-mail</span>
          <input
            type="text"
            name="email"
            value={email}
            onChange={this.handleInputChange}
          />

          <span>Senha</span>
          <input
            type="password"
            name="password"
            value={password}
            onChange={this.handleInputChange}
          />

          <Button size="big" type="submit">
            Entrar
          </Button>
        </SignForm>
      </Container>
    );
  }
}
