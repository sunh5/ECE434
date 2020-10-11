#include <linux/build-salt.h>
#include <linux/module.h>
#include <linux/vermagic.h>
#include <linux/compiler.h>

BUILD_SALT;

MODULE_INFO(vermagic, VERMAGIC_STRING);
MODULE_INFO(name, KBUILD_MODNAME);

__visible struct module __this_module
__attribute__((section(".gnu.linkonce.this_module"))) = {
	.name = KBUILD_MODNAME,
	.init = init_module,
#ifdef CONFIG_MODULE_UNLOAD
	.exit = cleanup_module,
#endif
	.arch = MODULE_ARCH_INIT,
};

#ifdef CONFIG_RETPOLINE
MODULE_INFO(retpoline, "Y");
#endif

static const struct modversion_info ____versions[]
__used
__attribute__((section("__versions"))) = {
	{ 0x516e49f9, "module_layout" },
	{ 0x73a7a766, "param_ops_uint" },
	{ 0xfe990052, "gpio_free" },
	{ 0x848cee4, "gpiod_unexport" },
	{ 0xb4f66f3b, "kthread_stop" },
	{ 0xe48cc71f, "wake_up_process" },
	{ 0x9a67bc9f, "kthread_create_on_node" },
	{ 0xda575cc, "gpiod_export" },
	{ 0x4e8b35ac, "gpiod_direction_output_raw" },
	{ 0x47229b5c, "gpio_request" },
	{ 0xf4e5e0ab, "kobject_put" },
	{ 0xa7b1f769, "sysfs_create_group" },
	{ 0xa0b6c3dd, "kobject_create_and_add" },
	{ 0x299cc41, "kernel_kobj" },
	{ 0x20c55ae0, "sscanf" },
	{ 0x84b183ae, "strncmp" },
	{ 0xdb7305a1, "__stack_chk_fail" },
	{ 0xf9a482f9, "msleep" },
	{ 0xddc1fca4, "gpiod_set_raw_value" },
	{ 0x395c5ae9, "gpio_to_desc" },
	{ 0xb3f7646e, "kthread_should_stop" },
	{ 0x7c32d0f0, "printk" },
	{ 0x8f678b07, "__stack_chk_guard" },
	{ 0x2e5810c6, "__aeabi_unwind_cpp_pr1" },
	{ 0x91715312, "sprintf" },
	{ 0xb1ad28e0, "__gnu_mcount_nc" },
};

static const char __module_depends[]
__used
__attribute__((section(".modinfo"))) =
"depends=";


MODULE_INFO(srcversion, "A0E9F4F4574EECDB13307A7");
