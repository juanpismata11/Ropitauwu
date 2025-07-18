import React from 'react';
import { IonContent, IonHeader, IonPage, IonTitle, IonToolbar } from '@ionic/react';
import Inputs from '../components/Inputs';
import './Login.css';
import { getUserService } from '../services/user';

const Login: React.FC = () => {
  return (
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
        <p>¿Es tu primera vez? <br/> <u>Registrate</u></p>
        <Inputs valor="user" nombre="Usuario" tipo ="text" />
        <Inputs valor="password" nombre="Contraseña" tipo ="password" />
        <button onClick={getUserService} className='btn-submit'>Iniciar Sesion</button>
      </IonContent>
    </IonPage>
  );
};

export default Login;
