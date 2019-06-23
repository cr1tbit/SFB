# SFB

When thinking of a name, i thought of BFG from DOOM, but instead for a small blog.

## About
>Please, do not expect to, like, gain any practical knowledge from this project. 

Let's analyze the description step-by-step:
| What  | Why  |
|---|---|
| Small | Just a couple of files!  |  
| markdown-enriched | Content can be written in markdown, and it is parsed runtime by [marked.js](https://github.com/markedjs/marked)|
| single-foldered   | For now everything is contained in very simple file structure. |
| pure-flasked      | Flask is used for serving static HTML and handle API requests.  |
| raw-html'd        | I'm terrified of npm, please respect that  |
| vanilla-vue.js'd  | I've found a vue.js lying on someone's server and referenced it in HTML.  |
| siimple-css'd     | [Fun CSS framework!](https://siimple.xyz/)  |
| barebashed        | Bash script generates article stubs so the user won't mess up some metadata.  |
| personal          | It's just my silly project, like the infamous [mf-website](https://motherfuckingwebsite.com/) but for fullstack developing.|

## How to deploy this bad boy

1. Git clone
2. Create an article stub, by running  `./content/generate_article_stub.sh <category> <article title>`
3. Adjust `run.sh`
4. Run `run.sh`
5. Navigate to `http://localhost:<port>/`

If you're lucky eneough, something nice might be rendered by your browser.

## License

>full license content will be published shortly.

© 2019 Jakub Sadowski | ΞΔ-flavoured MIT
