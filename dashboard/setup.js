const { execSync } = require('child_process');
const fs = require('fs');

const venvDir = 'venv';

console.log('🚀 Iniciando o setup do projeto...');

if (fs.existsSync(venvDir)) {
    console.log(`✅ Ambiente virtual já existe: ${venvDir}`);
} else {
    console.log('📦 Criando ambiente virtual...');
    execSync('python -m venv venv', { stdio: 'inherit' });
}

console.log('⚙️  Ativando ambiente virtual e instalando dependências...');

try {
    execSync('venv/bin/pip install --upgrade pip', { stdio: 'inherit' });
    execSync('venv/bin/pip install -r requirements.txt', { stdio: 'inherit' });
    console.log('✅ Setup concluído!');
    console.log('👉 Para ativar o ambiente virtual manualmente:');
    console.log('source venv/bin/activate');
} catch (err) {
    console.error('❌ Ocorreu um erro:', err);
}
