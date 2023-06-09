

console.log("It works");

let theme = localStorage.getItem('theme')

if(theme == null){
    setTheme('light')
}else{
    setTheme(theme)
}

let themeDots = document.getElementsByClassName("theme-dot")

for (var i=0; themeDots.length > i; i++)
{
    themeDots[i].addEventListener('click', function(){
        let mode  = this.dataset.mode
        console.log("Option clicked", mode);
        setTheme(mode);
    })
}

function setTheme(mode){
    if(mode == 'light'){
        document.getElementById('theme-style').href = "{% static 'css/default.css' %}";
    }

    else if(mode == 'blue'){
        document.getElementById('theme-style').href = "{% static 'css/blue.css' %}";
    }

    else if(mode == 'purple'){
        document.getElementById('theme-style').href = "{% static 'css/purple.css' %}";
    }

    else if(mode == 'green'){
        document.getElementById('theme-style').href = "{% static 'css/green.css' %}";
    }

    localStorage.setItem('theme', mode)
}