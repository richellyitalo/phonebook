import React from 'react';
import { BrowserRouter, Switch, Route } from 'react-router-dom';
import SignIn from '../pages/Auth/SignIn/SignIn';
import SignUp from '../pages/Auth/SignUp/SignUp';
import Main from '../pages/Main/Main';

const Routes = () => (
  <BrowserRouter>
    <Switch>
      <Route path="/signin" component={SignIn} />
      <Route path="/signup" component={SignUp} />
      <Route path="/" exact component={Main} />
    </Switch>
  </BrowserRouter>
);

export default Routes;
