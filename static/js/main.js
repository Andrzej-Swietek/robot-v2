window.addEventListener('DOMContentLoaded', () => {
    const socket = io.connect('http://127.0.0.1:5000');

	socket.on('connect', function() {
		socket.send('User has connected!');
	});

	socket.on('message', function(msg) {
		// $("#messages").append('<li>'+msg+'</li>');
		console.log('Received message');
	});

    let directions = ['up', 'left', 'right', 'back'];

    directions.forEach( dir => {
        document.querySelector(`.arrow.${dir}`).addEventListener('click', ()=>{
            socket.send(`${dir}`);
        });
    })

});