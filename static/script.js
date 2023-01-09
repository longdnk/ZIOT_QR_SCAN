const success = result => {
    const currentDate = new Date();
    const datetime = currentDate.getDate() + "/"
        + (currentDate.getMonth() + 1) + "/"
        + currentDate.getFullYear() + " At "
        + currentDate.getHours() + ":"
        + currentDate.getMinutes() + ":"
        + currentDate.getSeconds();
    document.getElementById('result').innerHTML = `
    <img class="iconSuccess" src="https://cdn-icons-png.flaticon.com/512/5709/5709755.png" alt="successIcon">
    <h2>Scan Success!</h2>
    <h3>Running progress email please wait</h3>
    <p name="${result}"><a href="${result}">${result}</a></p>
    <p>${datetime}</p>
    <div hidden="hidden">
        <form method="post" action="/contact">
            <div>
                <input name="fullname" type="text" class="form-control" value="${result}">
            </div>
            <div>
                <input name="datecheck" type="text" class="form-control" value="${datetime}">
            </div>
            <button type="submit" id="btnSubmit">Click here</button>
        </form>
    </div>
    <div class="containerOnStart">
        <div class="progress-bar"></div>
    </div>
    `;
    const elementClick = document.getElementById("btnSubmit");
    upload();
    elementClick.click();
    scanner.clear();
    document.getElementById('reader').remove()
}

const error = () => {
    console.error("Check Error");
}

const scanner = new Html5QrcodeScanner('reader', {
    qrbox: {
        width: '100%',
        height: '100%',
    },
    fps: 60,
});
scanner.render(success);

const upload = async () => {
    let index = 0;
    const progressBar = document.querySelector('.progress-bar')
    await progressBar.setAttribute('id', 'play-animation')
}
