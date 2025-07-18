import React from 'react';
import {IonPage, IonTitle, IonHeader, IonToolbar, IonContent } from '@ionic/react';
import './Login.css'
import Inputs from '../components/Inputs';
import {postUserService} from '../services/user';

const Register: React.FC = () => {
  return(
    <IonPage>
      <IonHeader>
        <IonToolbar>
          <IonTitle>User</IonTitle>
        </IonToolbar>
      </IonHeader>
      <IonContent fullscreen>
        <IonHeader collapse="condense">
          <IonToolbar>
            <IonTitle size="large">Iniciar Sesion</IonTitle>
          </IonToolbar>
        </IonHeader>
        <p>¿Ya tienes una cuenta? <br/> <u>Inicia Sesion</u></p>
        <Inputs valor="new-user" nombre="Usuario" tipo ="text" />
        <Inputs valor="new-password" nombre="Contraseña" tipo ="password" />
        <Inputs valor='new-password2' nombre="Confirmar Contrasena" tipo="password" />
        <button onClick={postUserService} className='btn-submit'>Registrarse</button>
      </IonContent>
    </IonPage>
  );
};

export default Register;