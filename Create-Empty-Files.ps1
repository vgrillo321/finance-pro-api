# 1) Carpetas que hay que crear
$folders = @(
    "app",
    "app\api",
    "app\db",
    "app\db\models",
    "app\core",
    "app\services",
    "app\services\parsing"
)

# Crear carpetas
$folders | ForEach-Object {
    New-Item -Path $_ -ItemType Directory -Force | Out-Null
}

# 2) Files que hay que crear
$files = @(
    "app\main.py",
    "app\api\routes.py",
    "app\db\base.py",
    "app\db\session.py",
    "app\db\models\user.py",
    "app\db\models\account.py",
    "app\db\models\category.py",
    "app\db\models\transaction.py",
    "app\core\config.py",
    "app\core\utils.py",
    "app\services\parsing\chase_csv.py",
    "app\services\parsing\capital_one_csv.py",
    "alembic.ini"
)

# Crear files
$files | ForEach-Object {
    New-Item -Path $_ -ItemType File -Force | Out-Null
}
