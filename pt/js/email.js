function email(){
    const email = 'contact.rodrigo.onofri@gmail.com';

    //Use the cliboard api to copy the email when click in the image
    navigator.clipboard.writeText(email)
    .then(() => {
        alert('Email copiado para a área de transferência!');
    })
    .catch((err) => { 
        console.error('Error copying email:', err);
        alert('Falha ao copiar email!');
    });
}