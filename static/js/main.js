window.addEventListener('DOMContentLoaded', () => {
    const IP = '192.168.43.101';
    const socketAddress = `http://${IP}:5000`;
    console.log(socketAddress)
    const socket = io.connect(socketAddress);
    
    socket.on('connect', function () {
        socket.send('User has connected!');
    });

    socket.on('message', function (msg) {
        // $("#messages").append('<li>'+msg+'</li>');
        console.log('Received message');
    });

    let directions = ['up', 'left', 'right', 'back'];

    let interval;

    directions.forEach(dir => {
        document.querySelector(`.arrow.${dir}`).onmouseover = () => {
            
            interval = setInterval(() => {
                socket.send(`${dir}`);
            }, 100)
        }

        document.querySelector(`.arrow.${dir}`).onmouseout = () => {
            clearInterval(interval);
        }
    })


    addGid()
});
