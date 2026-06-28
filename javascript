// servidor.js

const express = require('express');
const aplicacion = require('express')();

aplicacion.use(require('express').json());

aplicacion.get('/', (solicitud, respuesta) => {
    respuesta.json({
        proyecto: 'MENFANormativas',
        version: '1.0',
        descripcion: 'Plataforma de normativas aplicadas a la industria petrolera'
    });
});

aplicacion.listen(3000, () => {
    console.log('MENFANormativas ejecutándose en puerto 3000');
});
