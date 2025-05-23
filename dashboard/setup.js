const { execSync } = require('child_process');
const fs = require('fs');
const os = require('os');

const isWindows = os.platform() === 'win32';
const venvDir = 'venv';

console.log('🚀 Iniciando o setup do projeto...');

if (fs.existsSync(venvDir)) {
    console.log(`✅ Ambiente virtual já existe: ${venvDir}`);
} else {
    console.log('📦 Criando ambiente virtual...');
    execSync('python -m venv venv', { stdio: 'inherit' });
}

console.log('⚙️  Instalando dependências...');

try {
    const pipCmd = isWindows ? 'venv\\Scripts\\pip.exe' : 'venv/bin/pip';
    execSync(`${pipCmd} install --upgrade pip`, { stdio: 'inherit' });
    execSync(`${pipCmd} install -r requirements.txt`, { stdio: 'inherit' });

    console.log('✅ Setup concluído!');

    if (isWindows) {
        console.log('👉 Para ativar o ambiente virtual:');
        console.log('CMD:      venv\\Scripts\\activate.bat');
        console.log('PowerShell: venv\\Scripts\\Activate.ps1');
    } else {
        console.log('👉 Para ativar o ambiente virtual:');
        console.log('source venv/bin/activate');
    }

} catch (err) {
    console.error('❌ Ocorreu um erro:', err.message);
}
