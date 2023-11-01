<?php

namespace App\Http\Controllers;

use App\Models\Cliente;
use App\Models\Endereco;
use Illuminate\Foundation\Auth\Access\AuthorizesRequests;
use Illuminate\Foundation\Validation\ValidatesRequests;
use Illuminate\Routing\Controller as BaseController;
use Illuminate\Http\Request;

class Controller extends BaseController
{
    use AuthorizesRequests, ValidatesRequests;
    public function criarendereco(){
        return view("welcome");
    }
    public function criar(Request $request){
        $endereco = new Endereco();
        $endereco->cep = $request->input("cep");
        $endereco->uf = $request->input("uf");
        $endereco->cidade = $request->input("cidade");
        $endereco->bairro = $request->input("bairro");
        $endereco->rua = $request->input("rua");
        $endereco->numero = $request->input("numero");
        $endereco->complemento = $request->input("complemento");
        $endereco->save();

        $cliente = new Cliente();
        $cliente->name = $request->input("nome");
        $cliente->email = $request->input("email");
        $cliente->telefone = $request->input("telefone");
        $cliente->endereco_id = $endereco->id;
        $cliente->save();
        return redirect("/")->with("success","Cadastrado com sucesso");

    }
     public function lista(){
        $cliente = Cliente::select(
            'cliente.id',
            'cliente.name',
            'cliente.telefone',
            'cliente.email',
            'endereco.cep',
            'endereco.uf',
            'endereco.cidade',
            'endereco.bairro',
            'endereco.rua',
            'endereco.numero',
            'endereco.complemento'
        )
        ->join('endereco', 'endereco.id', '=', 'cliente.endereco_id')
        ->get();

        return view("lista", compact("cliente"));
     }

    public function editar($id){
        $cliente = Cliente::select(
            'cliente.id',
            'cliente.name',
            'cliente.telefone',
            'cliente.email',
            'endereco.cep',
            'endereco.uf',
            'endereco.cidade',
            'endereco.bairro',
            'endereco.rua',
            'endereco.numero',
            'endereco.complemento'
        )
        ->join('endereco', 'endereco.id', '=', 'cliente.endereco_id')
        ->where('cliente.id','=', $id)
        ->get();

        return view("editar", compact("cliente"));

    }
    public function update(Request $request, $id){
    
        $cliente =  Cliente::find($id);
        $cliente->name = $request->input("nome");
        $cliente->email = $request->input("email");
        $cliente->telefone = $request->input("telefone");
        $cliente->update();

        $endereco =  Endereco::find($cliente->endereco_id);
        $endereco->cep = $request->input("cep");
        $endereco->uf = $request->input("uf");
        $endereco->cidade = $request->input("cidade");
        $endereco->bairro = $request->input("bairro");
        $endereco->rua = $request->input("rua");
        $endereco->numero = $request->input("numero");
        $endereco->complemento = $request->input("complemento");
        $endereco->update();

        return redirect("/")->with("success","Atualizado com sucesso");
    }
    public function deletar($id){
        $cliente =  Cliente::find($id);
        $endereco =  Endereco::find($cliente->endereco_id);
        $cliente->delete();
        $endereco->delete();
        return redirect("/")->with("danger","Deletado com sucesso");

    }
}
