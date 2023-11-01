<html>
    <head>
    <title>Cadastro de Cliente</title>
    <meta http-equiv="Content-Type" content="text/html; charset=utf-8" />
    <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.2/dist/css/bootstrap.min.css" rel="stylesheet" integrity="sha384-T3c6CoIi6uLrA9TneNEoa7RxnatzjcDSCmG1MXxSR1GAsXEV/Dwwykc2MPK8M2HN" crossorigin="anonymous">

    <!-- Adicionando Javascript -->
    <script>
    
    function limpa_formulário_cep() {
            //Limpa valores do formulário de cep.
            document.getElementById('rua').value=("");
            document.getElementById('bairro').value=("");
            document.getElementById('cidade').value=("");
            document.getElementById('uf').value=("");
            document.getElementById('ibge').value=("");
    }

    function meu_callback(conteudo) {
        if (!("erro" in conteudo)) {
            //Atualiza os campos com os valores.
            document.getElementById('rua').value=(conteudo.logradouro);
            document.getElementById('bairro').value=(conteudo.bairro);
            document.getElementById('cidade').value=(conteudo.localidade);
            document.getElementById('uf').value=(conteudo.uf);
            document.getElementById('ibge').value=(conteudo.ibge);
        } //end if.
        else {
            //CEP não Encontrado.
            limpa_formulário_cep();
            alert("CEP não encontrado.");
        }
    }
        
    function pesquisacep(valor) {

        //Nova variável "cep" somente com dígitos.
        var cep = valor.replace(/\D/g, '');

        //Verifica se campo cep possui valor informado.
        if (cep != "") {

            //Expressão regular para validar o CEP.
            var validacep = /^[0-9]{8}$/;

            //Valida o formato do CEP.
            if(validacep.test(cep)) {

                //Preenche os campos com "..." enquanto consulta webservice.
                document.getElementById('rua').value="...";
                document.getElementById('bairro').value="...";
                document.getElementById('cidade').value="...";
                document.getElementById('uf').value="...";
                document.getElementById('ibge').value="...";

                //Cria um elemento javascript.
                var script = document.createElement('script');

                //Sincroniza com o callback.
                script.src = 'https://viacep.com.br/ws/'+ cep + '/json/?callback=meu_callback';

                //Insere script no documento e carrega o conteúdo.
                document.body.appendChild(script);

            } //end if.
            else {
                //cep é inválido.
                limpa_formulário_cep();
                alert("Formato de CEP inválido.");
            }
        } //end if.
        else {
            //cep sem valor, limpa formulário.
            limpa_formulário_cep();
        }
    };

    </script>
    <style>
         body{
            background-color: pink;
         }
        .centro{
            width: 70%;
            position: absolute;
            left: 30%;
        }
    </style>
    </head>

    <body>
    <!-- Inicio do formulario -->
    <br>
    <h1 style="text-align: center;" >Cadastro de Cliente</h1>
    <hr>
    <div class="centro">
      
      <form method="post" action="{{route('criarendereco')}}">
        @csrf
        <label class="form-label">Nome:
            <input name="nome" type="text" id="nome"class="form-control" size="60" /></label><br />
            <label class="form-label">Email:
                <input name="email" type="text" class="form-control" id="email" size="60" /></label><br />
                <label>Telefone:
                    <input name="telefone" type="text" class="form-control"id="telefone" size="60" /></label><br />
        <label class="form-label">Cep:
        <input name="cep" type="text" id="cep" class="form-control" value="" size="10" maxlength="9"
               onblur="pesquisacep(this.value);" /></label><br />
        <label class="form-label">Rua:
        <input name="rua" type="text" id="rua" class="form-control" size="60" /></label><br />
        <label class="form-label">Bairro:
        <input name="bairro" type="text" class="form-control" id="bairro" size="40" /></label><br />
        <label class="form-label">Cidade:
        <input name="cidade" type="text" class="form-control"id="cidade" size="40" /></label><br />
        <label class="form-label">Estado:
        <input name="uf" type="text" class="form-control" id="uf" size="2" /></label><br />
        <label class="form-label">Número:
            <input name="numero"  class="form-control"type="text"  size="50" /></label><br />
        <label class="form-label">Complemento:
                <input name="complemento" class="form-control" type="text"  size="50" /></label><br />
    
        <input name="ibge" type="HIDDEN" id="ibge" size="8" /></label><br />
        <button type="submit" class="btn btn-primary">Salvar</button> 
    </form>
</div>
    </body>

    </html>