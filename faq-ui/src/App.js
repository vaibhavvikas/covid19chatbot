import React from 'react';
import './App.css';
import { Widget } from 'rasa-webchat';
import { makeStyles } from '@material-ui/core/styles';
import AppBar from '@material-ui/core/AppBar';
import Toolbar from '@material-ui/core/Toolbar';
import Typography from '@material-ui/core/Typography';
import Button from '@material-ui/core/Button';

const useStyles = makeStyles((theme) => ({
  root: {
    flexGrow: 1,
  },
  menuButton: {
    marginRight: theme.spacing(2),
  },
  title: {
    flexGrow: 1,
  },
}));

function App() {

  const classes = useStyles();

  return (
    <div className="App">

      <AppBar position="static">
        <Toolbar>
          <Typography variant="h6" className={classes.title}>
          Covid-19 Enquiry
          </Typography>
          <Button color="inherit">Login</Button>
        </Toolbar>
      </AppBar>

      <Widget
      initPayload={"/greet"}
      subtitle={"Covid-19 Enquiry"}
      socketUrl={"http://localhost:5005"}
      socketPath={"/socket.io/"}
      profileAvatar={"https://icon-library.com/images/avatar-icon-images/avatar-icon-images-4.jpg"}
      customData={{"language": "en"}}
      title={"Enquiry"}
      />
    </div>

  );
}
export default App;
