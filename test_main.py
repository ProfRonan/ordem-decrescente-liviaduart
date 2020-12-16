"""Esse módulo é utilizado para realizar testes automáticos dos exercícios."""

import unittest
from unittest.mock import call, patch
import main


class Test(unittest.TestCase):
    """Classe para agregar os métodos que serão utilizados para testar."""
    def test_abc(self):
        """Função que testa ABC -> CBA."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['A', 'B', 'C']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 3
            calls = [call('C'), call('B'), call('A')]
            mock_print.assert_has_calls(calls)

    def test_213(self):
        """Função que testa 213 -> 321."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['2', '1', '3']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 3
            calls = [call('3'), call('2'), call('1')]
            mock_print.assert_has_calls(calls)

    def test_zazbzc(self):
        """Função que testa zc zb za -> zc zb za."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['zc', 'zb', 'za']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 3
            calls = [call('zc'), call('zb'), call('za')]
            mock_print.assert_has_calls(calls)

    def test_zbzcza(self):
        """Função que testa zb zc za -> zc zb za."""
        # Lista de valores que serão retornados pela função input.
        input_returns = ['zb', 'zc', 'za']
        with patch('builtins.input',
                   side_effect=input_returns) as mock_input, patch(
                       'builtins.print') as mock_print:
            main.main()
            # O teste se a saída corresponde ao especificado fica aqui.
            assert mock_input.call_count == 3
            calls = [call('zc'), call('zb'), call('za')]
            mock_print.assert_has_calls(calls)


if __name__ == '__main__':
    unittest.main()
