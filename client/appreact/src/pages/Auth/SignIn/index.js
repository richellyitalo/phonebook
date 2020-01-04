import React, { Component } from 'react';
import PropTypes from 'prop-types';

import { Container, SignForm } from '../styles';
import Button from '../../../styles/components/Button';

import { connect } from 'react-redux';
import { bindActionCreators } from 'redux';
import AuthActions from '../../../store/ducks/auth';

class SignIn extends Component {
  static propTypes = {
    signInRequest: PropTypes.func.isRequired
  };

  state = {
    username: '',
    password: ''
  };

  handleSubmit = e => {
    e.preventDefault();

    const { username, password } = this.state;
    const { signInRequest } = this.props;
    console.log('vai');
    signInRequest(username, password);
  };

  handleInputChange = e => {
    this.setState({ [e.target.name]: e.target.value });
  };

  render() {
    const { username, password } = this.state;

    return (
      <Container>
        <SignForm onSubmit={this.handleSubmit}>
          <h1>Bem vindo</h1>

          <span>E-mail</span>
          <input
            type="text"
            name="username"
            value={username}
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

const mapDispatchToProps = dispatch =>
  bindActionCreators(AuthActions, dispatch);

export default connect(null, mapDispatchToProps)(SignIn);
