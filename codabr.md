<h1>CodaBR</h1>
<h3>principais links e ideias dos workshops a que fui</h3>
<h4>sábado, 25 de novembro</h4>
<b>ddj whatsapp group</b>
<b>ddj whatsapp group</b>
<p>podcasts</p>
<ul>
  <li>https://www.hackedpodcast.com/</li>
  <li>https://www.oreilly.com/topics/oreilly-programming-podcast</li>
  <li>https://www.oreilly.com/topics/oreilly-data-show-podcast</li>
</ul>


<b>toolkit essencial do lobo solitário - juan torres (escola de dados)</b>
</br>
<ul>
  <li>http://dataviz.tools/</li>
  <li>http://www.visualisingdata.com/</li>
  <li>https://datavizcatalogue.com/</li>
 </ul>
 <p>busca avançada do google</p>
 <p>o que procurar:</p>
 <ul>
  <li>padrões</li>
  <li>valores médios</li>
  <li>pontos fora da curva</li>
  <li>extremos</li>
  <li>tendências (séries temporais)</li>
  <li>se o desvio padrão é alto, a média não é muito representativa</li>
  <li>no google sheets, a fórmula desvpad calcula o desvio padrão</li>
 </ul>
 
 <p>para usar com o google sheets:
 https://chrome.google.com/webstore/detail/power-tools/dofhceeoedodcaheeoacmadcpegkjobi</p>
 
 <p>para analisar a raça/cor da população brasileira por municípios e encontrar outros datasets:
  https://sidra.ibge.gov.br/</p>
  
  <p>para ajudar na limpeza de dados do google sheets:
  https://www.aubrett.com/article/information-technology/productivity/google-docs/left-mid-right</p>

<b>mentiras, mentiras deslavadas e estatísticas - daniel mariani</b>
</br>
<ul>
  <li>https://www.youtube.com/watch?v=14VYnFhBKcY</li>
</ul>

<b>Graph Databases: Discutindo o Relacionamento dos seus Dados com Python</b>
<p>install neo4j and python 3</p>
<ul>
  <li>https://github.com/nicysneiros/palestra-graph-db</li>
  <li>https://medium.com/labcodes/graph-databases-discutindo-o-relacionamento-dos-seus-dados-com-python-79688b557eec</li>
  <li>https://speakerdeck.com/labcodes/graph-databases-discutindo-o-relacionamento-dos-seus-dados-com-python</li>
  
  CREATE (joao:User {name:"Joao", idade:"24"})
  RETURN joao
  
  CREATE (gcaesar:User {name:"Joana", idade:"25", genero:"f" })
  RETURN gcaesar

  MATCH (gcaesar:User {name:"Gabriela"}), (joao:User {name:"Joao"})
  CREATE (gcaesar)-[r:FOLLOWS {date:"28-11-25"}]->(joao)
  RETURN gcaesar, joao
  
  MATCH (n1)-[:FRIENDS_WITH]->(n2)
  RETURN n1, n2
  
  <h4>domingo, 26 de novembro</h4>
  <p>work in progress</p>
