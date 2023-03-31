<!DOCTYPE-html>
<html>
<head>
    <title>{{title[0]}}</title>
</head>
<body>
    <h1>{{title[0]}}</h1>
    <hr>
    <br>
    <div class="all">
        <a href="{{title[1]}}">back</a>
        <div>
            %for item in food:
                <p class="title">{{item['name'][1:-1]}}</p>
                <p>ingredients: <small>{{item['ingredients'][1:-1]}}</small><br>
                recipe: <small><a href={{item['recipe'][1:-1]}} target="_blank">{{item['recipe'][1:-1]}}</a></small></p>
                <br>
            %end
        </div>
    </div>
    <div class="bottombar">
        <p>powered by Brainswu Recipe Puppy API</p>
    </div>
</body>
</html>

<style>
    body { font-size: 200%; font-family: sans-serif; }
    h1 { text-align: center; }
    .title { font-weight: 600; }
    .all { padding-left: 5%; }
    p { font-size: 75%; }
    .bottomBar { font-size: 50%; position: fixed; bottom: 0; left: 0; width: 100%; background-color: #878f99; text-align: center; }
</style>